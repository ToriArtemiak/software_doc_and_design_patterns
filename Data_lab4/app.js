const FileReader = require('./services/FileReader');
const FileWriter = require('./services/FileWriter');

const ConsoleStrategy = require('./strategies/ConsoleStrategy');
const KafkaStrategy = require('./strategies/KafkaStrategy');
const RedisStrategy = require('./strategies/RedisStrategy');

const config = require('./config/config.json');

// factory для вибору стратегії
function getStrategy(type) {
    switch (type) {
        case 'console':
            return new ConsoleStrategy();
        case 'kafka':
            return new KafkaStrategy();
        case 'redis':
            return new RedisStrategy();
        default:
            throw new Error("Unknown strategy");
    }
}

// 1. читаємо файл
const data = FileReader.read('./data/input.csv');

// 2. записуємо у файл
FileWriter.write('./data/output.csv', data);

// 3. вибираємо стратегію
const strategy = getStrategy(config.output);

// 4. вивід
strategy.output(data);