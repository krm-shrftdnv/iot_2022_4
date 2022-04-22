package com.example.demo.repository;

import com.example.demo.model.Control;
import com.example.demo.model.Indications;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface IndicationsRepository extends JpaRepository<Indications, Long> {
    @Query("select i from Indications i where i.tVOC > :tvoc or i.CO2 > :co2")
    List<Indications> findByCO2AfterAndTVOCAfter(@Param("co2") int co2, @Param("tvoc") int tvoc);
}
