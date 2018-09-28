const webpack = require('webpack');
const config = {
    entry:  __dirname + '/js/index.js',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
        {
          test: /\.js?/,
          exclude: /node_modules/,
          use: 'babel-loader'
        },
        {
          test: /\.css/,
          loader: 'style-loader!css-loader'
        }
      ]
    }
};
module.exports = config;
