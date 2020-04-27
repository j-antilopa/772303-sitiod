package com.example.lab8.repository;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.time.LocalDateTime;
import java.util.List;

public interface LogsRepository extends MongoRepository<Logs, ObjectId> {

    //task2
    @Query(value = "{'url': '?0'}, {'id': False, 'ip': True}")
    List<Logs> getAllByUrl(String url);

    //task3
    @Query(value = "{'start': {'$lte': '?0'}}")
    List<Logs> findAllByStartDateAfter(LocalDateTime start);

    List<Logs> findAllByStartAfter(LocalDateTime start);

    //task4
    @Query(value = "{'ip': '?0'}")
    List<Logs> findAllByIp(String ip);



}
