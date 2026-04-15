const fs = require('fs');

class FileWriter {
    static write(filePath, data) {
        fs.writeFileSync(filePath, data.join('\n'));
    }
}

module.exports = FileWriter;