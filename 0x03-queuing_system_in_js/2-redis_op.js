import redis from "redis";

const redisClient = redis.createClient();

redisClient.on('connect', function() {
	console.log("Redis client connected to the server");
});

redisClient.on("error", function(err) {
	console.log(`Redis client not connected to the server: ${err}`);
})


function setNewSchool(schoolName, value) {
	redisClient.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
	await redisClient.get(schoolName, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
