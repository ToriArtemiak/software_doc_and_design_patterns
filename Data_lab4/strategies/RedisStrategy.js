const OutputStrategy = require('./OutputStrategy');

class RedisStrategy extends OutputStrategy {
    output(data) {
        console.log("Saving to Redis...");
        data.forEach(line => {
            console.log(`Redis: ${line}`);
        });
    }
}

module.exports = RedisStrategy;