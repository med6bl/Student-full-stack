package com.example.demo.controller;

import com.example.demo.entity.University;
import com.example.demo.service.UniversityService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/universities")
@CrossOrigin(origins = "*")
public class UniversityController {

    private final UniversityService service;

    public UniversityController(UniversityService service) { this.service = service; }

    @GetMapping
    public List<University> list() { return service.list(); }

    @PostMapping
    public University create(@RequestBody University u) { return service.create(u); }

    @GetMapping("/{id}")
    public University get(@PathVariable Long id) { return service.findById(id).orElse(null); }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) { service.delete(id); }
}
