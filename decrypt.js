var crypto = require('crypto');

var decrypt = function (text, password){
    var decipher = crypto.createDecipher('aes-256-cbc',password);
    var dec = decipher.update(text,'hex','utf8');
    dec += decipher.final('utf8');
    return dec;
}

console.log(decrypt(process.argv[2], process.argv[3]));
