package com.example.lab8.repository;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "logs")
public class Logs {

    @NonNull
    private String ip;

    @NonNull
    private String url;

    @NonNull
    private LocalDateTime start;

    @NonNull
    private String duration;

}
