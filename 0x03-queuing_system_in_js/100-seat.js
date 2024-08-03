import redis from "redis";
import kue from "kue";
import express from "express";
import { promisify } from "util";

const queue = kue.createQueue();
const client = redis.createClient();
const server = express();

client.on('connect', function() {
    console.log("Redis client connected to the server");
});

client.on("error", function(err) {
    console.log(`Redis client not connected to the server: ${err}`);
})

const reserveSeat = promisify(client.set).bind(client);
const getCurrentAvailableSeats = promisify(client.get).bind(client);

async function reserveSeatById(number) {
    await reserveSeat("available_seats", number);
}

reserveSeatById(50);

let reservationEnabled = true;

server.get("/available_seats", async (req, res) => {
    try {
        const numberOfAvailableSeats = await getCurrentAvailableSeats("available_seats");
        res.json({
            numberOfAvailableSeats,
        });
    } catch (err) {
        res.status(500).json({ status: 'Error fetching available seats', error: err.message });
    }
});

server.get("/reserve_seat", (req, res) => {
    if (!reservationEnabled) {
        return res.json({"status": "Reservation are blocked"});
    }

    const job = queue.create("reserve_seat").save(function(err) {
        if (!err) {
            return res.json({
                "status": "Reservation in process"
            });
        } else {
            return res.json({"status": "Reservation failed"});
        }
    });

    job.on("complete", function() {
        console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on("failure", function(err) {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
});

server.get("/process", (req, res) => {
    res.json({ "status": "Queue processing" });

    queue.process("reserve_seat", async (job, done) => {
        try {
            const currentSeats = await getCurrentAvailableSeats("available_seats");
            const currentSeatsInt = parseInt(currentSeats, 10);

            if (currentSeatsInt <= 0) {
                reservationEnabled = false;
                throw new Error("Not enough seats available");
            }

            const updatedSeats = currentSeatsInt - 1;
            await reserveSeatById(updatedSeats);

            if (updatedSeats === 0) {
                reservationEnabled = false;
            }

            done();
        } catch (err) {
            done(err);
        }
    });
});

server.listen(1245, () => {
    console.log("Server is running on port 1245");
});
