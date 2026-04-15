const fs = require('fs');

class FileReader {
    static read(filePath) {
        const data = fs.readFileSync(filePath, 'utf-8');
        return data.split('\n');
    }
}

module.exports = FileReader;