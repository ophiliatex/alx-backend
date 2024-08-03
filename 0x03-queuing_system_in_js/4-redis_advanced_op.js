import redis from "redis";

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', function() {
    console.log("Redis client connected to the server");
});

client.on('error', function(err) {
    console.log('Redis client not connected to the server: ', err);
});

// Use hSet to set hash fields
client.hSet("HolbertonSchools", "Portland", 50, redis.print);
client.hSet("HolbertonSchools", "Seattle", 80, redis.print);
client.hSet("HolbertonSchools", "New York", 20, redis.print);
client.hSet("HolbertonSchools", "Bogota", 20, redis.print);
client.hSet("HolbertonSchools", "Cali", 40, redis.print);
client.hSet("HolbertonSchools", "Paris", 2, redis.print);

client.hGetAll("HolbertonSchools", function(err, res) {
    if (err) {
        console.error("Error getting hash fields: ", err);
    } else {
        console.log("HolbertonSchools: ", res);
    }
    
    client.quit();
});
