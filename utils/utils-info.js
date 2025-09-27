const alerts = require('alerts-in-cli');
const clearLog = () => process.stdout.write(process.platform === 'win32' ? '\x1B[2J\x1B[0f' : '\x1B[2J\x1B[3J\x1B[H');
const checkVersion = (major) => {
    let currentVersion = process.version;
    let currentMajorVersion = Number(currentVersion.slice(1, 3))
    let nMajor = Number(major);

    if(currentMajorVersion < nMajor) {
        alerts({
            type: 'error',
            msg: 'Node version issue!'
        });
        alerts({
            type: 'info',
            msg: `Your are running Node version: ${currentVersion}`
        });
        alerts({
            type: 'info',
            msg: `Required version of Node is: v${major} or higher.`
        });
        process.exit();
    }
}
const unhandled = () => process.on('unhandledRejection', (err) => {
    alerts({
        type: 'error',
        msg: 'An error occurred please go to the error stack!',
        name: 'Unhandled Error'
    });
    console.log(err);
});
module.exports = {
    clearLog,
    checkVersion,
    unhandled
}
