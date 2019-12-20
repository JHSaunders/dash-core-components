const presets = [
    '@babel/preset-env',
    '@babel/preset-react'
];

const plugins = [
    '@babel/plugin-syntax-dynamic-import',
    '@babel/plugin-transform-async-to-generator',
    '@babel/plugin-transform-runtime'
];

// eslint-disable-next-line no-process-env
if (process.env.ENV === "test") {
    plugins.push("styled-jsx/babel-test");
} else {
    plugins.push("styled-jsx/babel");
}

module.exports = { presets, plugins };
