package com.example.demo.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.Date;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Entity
public class Indications {
    @Id
    @Column(name = "id", nullable = false)
    private Long id;

    private int CO2;
    private int tVOC;
    @JsonProperty(value = "created_at")
    private Date createdAt;
}