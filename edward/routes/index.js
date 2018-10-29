var express = require('express');
var router = express.Router();

const fs = require('fs');
const url = require('url');

var PATH = "/edward/public/data/";
//var PATH = "../results/";


// トップページのルーティング
router.get('/', function (request, response) {
  let imgFolders = [];
  fs.readdir(PATH, function(err, files){
      if (err) throw err;

      // ディレクトリから一覧を取得
      files.filter(function(file){
        var trgPath = PATH  + file;
        if(fs.existsSync(trgPath + "/img")){ // 学習のデータは参照しない．
            imgFolders.push( file + '.result' );
        }else if(fs.statSync(trgPath).isDirectory()){// ディレクトリが存在している時．
          var fileName = file;
          imgFolders.push( file + '.dir' );
        }
      });
    response.render('index', {imgFolders:imgFolders});
  });
});



// コンテンツページ
router.get('/*.result', function (request, response) {
  // URLからパスを解析
  const url_parts = url.parse(request.path);
  const rootFolder = url_parts.pathname.slice( 0, -7 );
  const imgPath = PATH + rootFolder  + '/img';
  const images = [];

  fs.readdir(imgPath, function(err, files){
    if (err) throw err;

    // ディレクトリから画像一覧を取得
    var fileList = files.filter(function(file){
      if(file.match(/.jpg/g) ){
        r_imgPath = PATH + "/" + file;
        r_imgPath = imgPath.replace("/edward/public","") + "/" + file
        frame = file.slice(0,-4)
        imgData = {
          path:r_imgPath,
          frame:frame,
          object:1
        }
        images.push( imgData );
      }
    });
    images.sort(
      function(a,b){
        var aName = Number(a["frame"]);
        var bName = Number(b["frame"]);
        if( aName < bName ) return -1;
        if( aName > bName ) return 1;
        return 0;
      }
    );
    response.render('look', { imgData:images});
  });
});


module.exports = router;
