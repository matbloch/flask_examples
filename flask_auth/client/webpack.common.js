const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const outputPath = path.resolve(__dirname, 'dist');

module.exports = {
  entry: {
    app: './src/index.js'
  },
  // generate bundle file that is served by the app
  output: {
      path: outputPath,
      filename: 'app.bundle.js'
  },
  // allows to ignore extension in imports
  resolve: {
    extensions: ['.js', '.jsx', '.css']
  },
  plugins: [
    // index html generation
    new HtmlWebpackPlugin({
      title: 'Authentication Client',
        favicon: '',
        template: './src/index.html'
    })
  ],
  module: {
    // modules to transform other languages to js
    // pipe every file with this extension through the specified loaders
    rules: [
      {
        // React.js and Ecma Script Transpiler
        test: /\.jsx?$/,
        include: path.resolve(__dirname, 'src'),
        use: [
            'cache-loader', // enable caching for heavy loaders
            {
          loader: 'babel-loader',
          options: {
            presets: ['env', 'stage-0', 'react']
          }
        }]
      },
    ]
  }
};
