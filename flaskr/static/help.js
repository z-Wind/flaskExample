$(document).ready(function(){ // 網頁載入完畢時，執行傳入的 function 物件
    $('.formCheck').submit(function(){
        str = ""
        interrupt = false
        $(this).find('input').each(function(){
            var isnullType = ['number', 'text', 'date'];
            if(isnullType.indexOf(this.type) >= 0)
            {
                if(this.value == "")
                {
                   alert(this.placeholder + " 不能為空")
                   interrupt = true
                   return false
                }
                str += (this.placeholder + ":" + this.value + "\n")
            }
            var nameType = ['file']
            if(nameType.indexOf(this.type) >= 0)
            {
                if(this.value == "")
                {
                   alert(this.name + " 不能為空")
                   interrupt = true
                   return false
                }
                str += (this.name + ":" + this.value + "\n")
            }
            var checkType = ['radio', 'checkbox'] 
            if(checkType.indexOf(this.type) >= 0)
            {
                if(this.checked)
                {
                    str += (this.name + ":" + this.value + "\n")
                }
            }
            
            if(this.type == "hidden")
            {
                
            }
        });
        if(interrupt)
           return false
        return confirm("確認送出？\n" + str)
    });
});
