const webpack = require('webpack');
const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const path = require('path');

module.exports = merge(common, {
  mode: 'development',
  // devtool: 'source-map',
  devtool: false,
  module: {
    rules: [
      {
        // css dev bundling options
        test: /\.(sa|sc|c)ss$/,
        use: [
            "style-loader", // creates style nodes from JS strings
            {  // translates CSS into CommonJS
              loader: "css-loader",
              options: {
                importLoaders: 1,   // allows sass @import() statements
              },
            },
            "sass-loader" // compiles Sass to CSS
        ]
      }
    ]
  },
  // webpack-dev-server configuration
  // serve content of /dist directly to localhost:8080
  devServer: {
      contentBase: path.join(__dirname, 'dist'),
      hot: true,  // hot reloading
      inline: true,
      host: 'localhost', // Defaults to `localhost`
      port: process.env.PORT || 8080, // Defaults to 8080
      stats: {
        color: true
      }
  },
  plugins: [
    new webpack.DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify('development')
    }),
    // enable hot reloading
    new webpack.HotModuleReplacementPlugin(),
  ]
});
