package com.example.lab8.service;

import com.example.lab8.helper.CSVReader;
import com.example.lab8.repository.Logs;
import com.example.lab8.repository.LogsRepository;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.mapreduce.MapReduceResults;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

@Service
public class LogsService implements ILogsService {

    private final LogsRepository logsRepository;
    private final MongoTemplate mongoTemplate;

    public LogsService(LogsRepository logsRepository,
                       MongoTemplate mongoTemplate) {
        this.logsRepository = logsRepository;
        this.mongoTemplate = mongoTemplate;
    }

    @Override
    public List<Logs> addLogs() {
        List<Logs> logsList = CSVReader.getLogsList();
        return logsRepository.saveAll(logsList);
    }

    public List<Logs> getAll() {
        return logsRepository.findAll();
    }

    public Set<String> getAllUrl() {
        List<Logs> logsList = logsRepository.findAll();
        return logsList.stream()
                .flatMap(p -> Stream.of(p.getUrl()))
                .collect(Collectors.toSet());
    }

    public Set<String> getAllIpByUrl(String url) {
        List<Logs> logsList = logsRepository.getAllByUrl(url);

        return logsList.stream()
                .flatMap(p -> Stream.of(p.getIp()))
                .collect(Collectors.toSet());
    }

    public Set<String> getAllUrlByDate(LocalDateTime start, LocalDateTime finish) {

//        List<Logs> logsList = logsRepository.findAllByStartDateAfter(start);
        List<Logs> logsList = logsRepository.findAllByStartAfter(start);
        return logsList.stream()
                .filter(a -> a.getStart().plusSeconds(Long.parseLong(a.getDuration())).isBefore(finish))
                .flatMap(p -> Stream.of(p.getUrl()))
                .collect(Collectors.toSet());
    }

    public Set<String> getAllUrlByIp(String ip) {
        List<Logs> logsList = logsRepository.findAllByIp(ip);
        return logsList.stream()
                .flatMap(p -> Stream.of(p.getUrl()))
                .collect(Collectors.toSet());
    }

    public String getAllUrlByDuration() {
        String map = "function() {emit(this.url, this.duration);};";
        String reduce = "function(url, duration) {return Array.sum(duration);};";

        MapReduceResults<String> sumResults = mongoTemplate.mapReduce(
                "logs",
                map,
                reduce,
                String.class
        );
        return sumResults.getRawResults().toJson();
    }

    public void deleteAll() {
        logsRepository.deleteAll();
    }

    public String getSumCount() {
        String map = "function() { emit(this.url, 1); };";
        String reduce = "function(url, count) {return count.length;};";

        MapReduceResults<String> sumResults = mongoTemplate.mapReduce(
                "logs",
                map,
                reduce,
                String.class
        );
        return sumResults.getRawResults().toJson();
    }

    public String getSumUrlTask7(LocalDateTime start, LocalDateTime finish) {
        String map = "function() { emit(this.url, 1); };";
        String reduce = "function(url, count) {return count.length;};";
        Query query = new Query(Criteria.where("start").lte(start).gte(finish));

        MapReduceResults<String> sumResults = mongoTemplate.mapReduce(
                query,
                "logs",
                map,
                reduce,
                String.class
        );
        return sumResults.getRawResults().toJson();
    }

}
