const OutputStrategy = require('./OutputStrategy');

class ConsoleStrategy extends OutputStrategy {
    output(data) {
        data.forEach(line => console.log(line));
    }
}

module.exports = ConsoleStrategy;