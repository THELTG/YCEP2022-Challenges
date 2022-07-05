// initialization 
// to install express:
// npm install express
var express=require('express');
var app=express();

// change as needed
const host = "localhost"
const port = 6969

// BED type shit
const cookie = "cookie=cH0c0lat3_cOoKiEs_aR3_bAd_f0r_yOu"
app.get("/", function(req,res){
    res.status(200)
    if (req.headers.cookie == cookie){
        res.cookie("cookie","cH0c0lat3_cOoKiEs_aR3_bAd_f0r_yOu",{maxAge: 10800})
        res.send("YUMMY!! YCEP22{i_hAt3_RaiS1n_c00k1es}")
    } else {
        res.cookie('cookie','h3alThy_rAisIn_co0kie',{maxAge: 10800})
        res.send("i want a CHOCOLATE cookie!: " + cookie)
    }
})

app.listen(port,host,function(){
    console.log(`Server is located at http://${host}:${port}`)
})