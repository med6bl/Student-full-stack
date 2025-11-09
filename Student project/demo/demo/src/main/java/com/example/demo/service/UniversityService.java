package com.example.demo.service;

import com.example.demo.entity.University;
import com.example.demo.repository.UniversityRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UniversityService {

    private final UniversityRepository repo;

    public UniversityService(UniversityRepository repo) {
        this.repo = repo;
    }

    public University create(University u) { return repo.save(u); }
    public List<University> list() { return repo.findAll(); }
    public Optional<University> findById(Long id) { return repo.findById(id); }
    public void delete(Long id) { repo.deleteById(id); }
}
