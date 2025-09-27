let meow = require("meow");
let { green, yellow, cyan, dim, white } = require("chalk");

let helperText = `
Usage:
  ${green('npx occt')} ${yellow('[--options]')} ${cyan('<command>')}

Options:
  ${yellow('-c')}, ${yellow('--compile')}       Pass flag for Compiled Code output file. ${dim("[Auto Detect OS and Programming, and save output file]")}
  ${yellow('-o')}, ${yellow('--output')}        Pass flag only used with -c flag, for output file coustome name.
  ${yellow('-i')}, ${yellow('--interpreted')}   Pass flag for interprate Code output only.
  ${yellow('-a')}, ${yellow('--args')}          After this flag all value consider as command line arguments.
  ${yellow('-d')}, ${yellow('--debug')}         Print debug information if needed.
  ${yellow('-v')}, ${yellow('--version')}       Print version information.
  ${yellow('-h')}, ${yellow('--help')}          Print the help information.
  ${yellow('--clear')}             Clear the terminal window. ${dim('(default: true)')}
  ${yellow('--no-clear')}          Don't clear the terminal window.

Commands:
  ${cyan('help')}              Print the help information.

Example:
  ${green('npx occt')} ${yellow('-c')} ${white('./main.cpp')} ${yellow('-o')} ${white('main')}
  ${green('npx occt')} ${yellow('-i')} ${white('./app.js')}

`;


module.exports = meow(helperText, {
    inferType: true,
    hardRejection: false,
    flags: {
        clear: {
            type: 'boolean',
            default: true
        },
        debug: {
            type: 'boolean',
            default: false,
            alias: 'd'
        },
        version: {
          type: 'boolean',
          default: false,
          alias: 'v'
        },
        help: {
          type: 'boolean',
          default: false,
          alias: 'h'
        },
        compile: {
          type: 'string',
          default: '',
          alias: 'c'
        },
        interpreted: {
          type: 'string',
          default: '',
          alias: 'i'
        },
        output: {
          type: 'string',
          default: '',
          alias: 'o'
        },
        args: {
          type: 'string',
          default: '',
          alias: 'a',
          isRequired: false
        }
    }
});