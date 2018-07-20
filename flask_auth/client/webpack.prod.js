const webpack = require('webpack');
const merge = require('webpack-merge');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const CleanWebpackPlugin = require('clean-webpack-plugin');
const common = require('./webpack.common.js');

module.exports = merge(common, {
    mode: 'production',
    stats: {
        colors: false,
        hash: true,
        timings: true,
        assets: true,
        chunks: true,
        chunkModules: true,
        modules: true,
        children: true,
    },
    devtool: 'source-map',  // TODO: needed?
    optimization: {
        minimizer: [
          new UglifyJSPlugin({
            cache: true,
            parallel: true,
            sourceMap: true // set to true if you want JS source maps
          }),
          new OptimizeCSSAssetsPlugin({})
        ]
    },
    plugins: [
        // cleanup build folder
        new CleanWebpackPlugin(['dist']),
        // define production env variable for 3rd party optimization
        // to check for mode in production: process.env.NODE_ENV === 'production'
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('production')
        }),
        // push styling to a separate file
        new MiniCssExtractPlugin({
          filename: "[name].[hash].css",
          chunkFilename: "[id].[hash].css"
        })
    ],
    module: {
        rules: [
            {
            test: /\.(sa|sc|c)ss$/,
            use: [
                    MiniCssExtractPlugin.loader,    // instead of style-loader in dev mode, to aggregate css
                    {  // translates CSS into CommonJS
                      loader: "css-loader",
                      options: {
                        importLoaders: 1,   // allows sass @import() statements
                      },
                    },
                    'sass-loader'
                ],
            }
        ]
    }

});
