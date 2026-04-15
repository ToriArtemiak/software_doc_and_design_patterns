const OutputStrategy = require('./OutputStrategy');

class KafkaStrategy extends OutputStrategy {
    output(data) {
        console.log("Sending to Kafka...");
        data.forEach(line => {
            // тут буде реальна відправка
            console.log(`Kafka: ${line}`);
        });
    }
}

module.exports = KafkaStrategy;