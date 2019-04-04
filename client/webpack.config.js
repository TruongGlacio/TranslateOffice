const HtmlWebpackPlugin = require('html-webpack-plugin');
const { resolve } = require('path')

module.exports = {
  entry: './src/index.js',

  output: {
    path: require('path').resolve('./build'),
		filename: 'bundle.js'
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loaders: ['babel-loader']
      },
      {
        test: /\.css$/,
        loaders: ['style-loader', 'css-loader']
      },
      {
        test: /\.(png|woff|woff2|eot|ttf|svg)$/,
        loaders: ['url-loader', 'img-loader']
      },
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: resolve(__dirname, 'public', 'index.html'),
      favicon: resolve(__dirname, 'public', 'favicon.ico'),
      manifest: resolve(__dirname, 'public', 'manifest.js')
    })
  ]
};
