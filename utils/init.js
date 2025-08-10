const chalk = require("chalk");
const { clearLog, checkVersion, unhandled } = require("./utils-info");
const pkgJSON = require("./../package.json");

module.exports = ({ clear }) => {
    // Clear the console
    clear && clearLog();

    // check the node version.
    checkVersion('12');

    // handle unhandled errors.
    unhandled();

    const cli = {
        title: ` OCCT `,
        tagLine: 'Learn more, inovate more!!',
        description: pkgJSON.description,
        version: pkgJSON.version,
        bgColor: `#FADC00`,
        color: `#000000`,
        token: require('solverjs').token()
    }

    console.log(`
${chalk.bold.bgHex(cli.bgColor).hex(cli.color)(cli.title)} ${ "v" + cli.version} ${chalk.dim(cli.tagLine)}\n${chalk.dim(cli.description)}
    `);
}