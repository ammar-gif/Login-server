package com.example.backend.Controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;
@RestController
public class test {

        @GetMapping({ "/registration"})
        public String showRegistrationForm() {
            return "Hallo omar here is your first controller";
        }
}
