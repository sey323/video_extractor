
class Dumper:
    def __init__(self):
        self.dump_text = ""
        self.bootstrap_cdn ='<head>\n \
                                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />\n \
                                <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n \
                                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\n \
                            </head>'
        self.begin = '<table class="table table-responsive">'
        self.end = '</table>'
        self.content = ''
        self.no = 1

    def add_scene(self,frame,time,param_path ):
        '''
        フレームごとのHTML構文を追加する．
         Parameters
        ----------
        frame : int
            検出したフレーム
        '''
        with open(param_path, "r",encoding='utf-8') as f:
            param_data = f.read()
        self.content += '<tr class="col-md-12">\n \
                            <td class="col-md-1">{0}</td>\n \
                            <td class="col-md-1">{1}</td>\n \
                            <td class="col-md-5">\n  \
                                <img class="gen-img" src="{2}">\n \
                            </td>\n \
                            <td class="col-md-4">{3}</td>\n \
                            <td class="col-md-2"></td>\n \
                        </tr>'.format(self.no, time,"img/"+str(frame)+".jpg",param_data)
        self.no += 1

    def save_html( self , save_path ):
        '''
        HTML形式で保存する．
        '''
        html = self.begin + self.content + self.end
        with open(save_path+'/index.html', mode='w') as f:
            f.write(html)
        print('html save complete!')
