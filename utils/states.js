const ora = require("ora");
const axios = require("axios");
const fs = require('fs');
const os = require('os');
const FormData = require('form-data');
const handelError = require("alerts-in-cli");
const BASE_SERVER_URL = "https://occt.in"

let spinner = ora({ text: '' });

const uploadingFileCompile = async (flags) => {
    spinner.start(`Uploading file and processing...`);
    try {
        const formData = new FormData();
        const os_info = os.platform() + " " + os.arch();
        if(os_info === "darwin arm64") {
            formData.append('os', "macos-arm64");
        }else if(os_info === "darwin x64") {
            formData.append('os', "macos-x64");
        }else if(os_info === "win32 x64") {
            formData.append('os', "windows-x64");
        }else if(os_info === "linux x64") {
            formData.append('os', "linux-x64");
        }else {
            formData.append('os', os_info);
        }
        formData.append('file', fs.createReadStream(flags.compile), flags.compile);
        if(flags.outputFile) {
            formData.append('outputName', flags.outputFile);
        }

        if (flags.args) {
            formData.append('args', JSON.stringify(flags.args));
        }

        const response = await axios.post(`${BASE_SERVER_URL}/compile`, formData, {
            headers: formData.getHeaders()
        });

        if (response.status !== 200) {
            console.error('Compilation failed:', response.statusText);
            process.exit(1);
        }

        if(response.status === 200) {
            // console.log('✅ Compilation result:', response.data);

            const downloadUrl = `${BASE_SERVER_URL}${response.data.download}`;
            const writer = fs.createWriteStream(response.data.download.replace("/download/", ""));

            const download = await axios.get(downloadUrl, { responseType: 'stream' });
            download.data.pipe(writer);

            writer.on('finish', () => console.log(`Compiled file: ${response.data.download.replace("/download/", "")}`));
        }
        spinner.stop();
    } catch (error) {
        spinner.fail();
        handelError({
            type: "error",
            msg: error.response.data.error || error,
            name: "API Call fail"
        });
        process.exit(1);
    }
}

const uploadingFileInterprate = async (flags, cli = {}) => {
    spinner.start(`Uploading file and processing...`);
    try {
        const formData = new FormData();
        formData.append('file', fs.createReadStream(flags.interpreted), flags.interpreted);
        if(flags.outputFile) {
            formData.append('outputName', flags.outputFile);
        }

        if (flags.args) {
            if((cli.input.length > 0) && (cli.flags.args.length > 0)) {
                flags.args += ` ${cli.input.join(' ')}`;
            }
            formData.append('args', JSON.stringify(flags.args + ''));
        }

        const response = await axios.post(`${BASE_SERVER_URL}/interprate`, formData, {
            headers: formData.getHeaders()
        });

        if (response.status !== 200) {
            console.error('Compilation failed:', response.statusText);
            process.exit(1);
        }

        if(response.status === 200) {
            // console.log('✅ Compilation result:', response.data);

            console.log(`\n---\n${response.data.output}---`);
        }
        spinner.stop();
    } catch (error) {
        spinner.fail();
        handelError({
            type: "error",
            msg: error.response.data.error || error,
            name: "API Call fail"
        });
        process.exit(1);
    }
}

module.exports = {
    uploadingFileCompile,
    uploadingFileInterprate
}