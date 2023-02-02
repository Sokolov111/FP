<?php


$arr = ['asd','asd','asd','asd',' ','asd'];


function func($ar){
    for($i=0;$i<count($ar);$i++){
        if($ar[$i] == " "){
            $asd =false;
        }

    }
    return $asd;
}
$ans= true;

while ($ans){
    $ans = func($arr);
}


// <label> Наименование организации *
//    [text text-343 placeholder "Наименование организации"]</label>



// <label> Должность *
//     [text text-344]</label>

// <label> Имя Фамилия участника *
//      [text text-345]</label>
    


// <label> E-mail адрес *
//     [email* email-230 ]</label>
     


// <label> Контактные данные *
//     [tel* tel-43 ]</label>


// <label> Город 
//     [text text-346 ] </label>
// [submit "Отправить"]
