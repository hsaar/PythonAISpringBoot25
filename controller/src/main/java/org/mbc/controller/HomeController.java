package org.mbc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller // url 분기를 담당
public class HomeController {

    @GetMapping("/")
    public String home(Model model){
        return "index"; // 요청이 온 후에 프론트를 전달
        // resources/templates/index.html 응답
    }
    
}
