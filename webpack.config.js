const path = require('path');

module.exports = {
    entry: './static/js/index.js',
    mode: 'development',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'static/js/'),
    },
};
