package com.example.lab8.helper;

import com.example.lab8.repository.Logs;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class CSVReader {

    private static final String fileName = "E:\\lab8\\src\\main\\resources\\data.csv";

    public static List<Logs> getLogsList() {
        List<Logs> logs = readLogsFromCSV(fileName);
        return logs;
    }

    private static List<Logs> readLogsFromCSV(String fileName) {
        List<Logs> logsList = new ArrayList<>();
        Path pathToFile = Paths.get(fileName);

        try (BufferedReader br = Files.newBufferedReader(pathToFile, StandardCharsets.US_ASCII)) {

            String line = br.readLine();

            while (line != null) {
                String[] attributes = line.split(",");
                Logs log = createLog(attributes);
                logsList.add(log);
                line = br.readLine();
            }
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }

        return logsList;
    }

    private static Logs createLog(String[] metadata) {
        String ip = metadata[0];
        String url = metadata[1];
        LocalDateTime start = LocalDateTime.parse(metadata[2]);
        String duration = metadata[3];

        return new Logs(ip, url, start, duration);
    }
}
