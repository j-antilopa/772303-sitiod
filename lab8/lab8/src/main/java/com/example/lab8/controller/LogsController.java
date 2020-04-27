package com.example.lab8.controller;

import com.example.lab8.repository.Logs;
import com.example.lab8.service.LogsService;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Set;

@RestController
@RequestMapping("/logs")
public class LogsController {

    private final LogsService logsService;

    public LogsController(LogsService logsService) {
        this.logsService = logsService;
    }

    @PostMapping
    public List<Logs> addLogs() {
        return logsService.addLogs();
    }

    @DeleteMapping
    public void deleteAll() {
        logsService.deleteAll();
    }

    @GetMapping
    public List<Logs> getAll() {
        return logsService.getAll();
    }

    //task1
    @GetMapping("/getAllUrl")
    public Set<String> getAllByUrl() {
        return logsService.getAllUrl();
    }

    //task2
    @GetMapping("/getAllIpByUrl")
    public Set<String> getAllIpByUrl(@RequestParam String url) {
        return logsService.getAllIpByUrl(url);
    }

    //task3
    @GetMapping("/getAllByDate")
    public Set<String> getAllByDate(@RequestParam @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss") LocalDateTime start,
                                    @RequestParam @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss") LocalDateTime finish) {
        return logsService.getAllUrlByDate(start, finish);
    }

    //task4
    @GetMapping("/getUrlByIp")
    public Set<String> getAllUrlByIp(@RequestParam String ip) {
        return logsService.getAllUrlByIp(ip);
    }

    //task5
    @GetMapping("/getAllUrlByDuration")
    public String getAllUrlByDuration() {
        return logsService.getAllUrlByDuration();
    }

    //task6
    @GetMapping("/getSumCount")
    public String getSumCount() {
        return logsService.getSumCount();
    }

    //task7
    @GetMapping("/getSumUrlTask7")
    public String getSumUrlTask7(@RequestParam @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss") LocalDateTime start,
                                 @RequestParam @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss") LocalDateTime finish) {
        return logsService.getSumUrlTask7(start, finish);
    }

}
