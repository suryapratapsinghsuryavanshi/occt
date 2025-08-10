#!/usr/bin/env node
const { spawnSync } = require('child_process');
let cli = require("./utils/cli");
let { uploadingFileCompile, uploadingFileInterprate } = require("./utils/states");

const flags = cli.flags;


(async () => {
    cli.input.includes('help') && cli.showHelp(0);
    require("./utils/init")({clear: flags.clear});

    // if compile flag is passed
    if (flags.compile) {
        uploadingFileCompile(flags);
    }

    // if interpreted flag is passed
    if (flags.interpreted) {
        uploadingFileInterprate(flags, cli);
    }

    // debug cli.
    flags.debug ? require("./utils/debug")(cli) : '';
})();
