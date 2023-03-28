package com.example.Login_server;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
//test
@RestController
public class Users_Controller {

    @GetMapping("Users")
    public String Getusers ()
    {
        return  "There are no users yet";
    }




}
