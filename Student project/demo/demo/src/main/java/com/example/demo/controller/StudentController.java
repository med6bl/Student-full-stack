package com.example.demo.controller;

import com.example.demo.entity.Student;
import com.example.demo.service.StudentService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/students")
@CrossOrigin(origins = "*")
public class StudentController {

    private final StudentService service;

    public StudentController(StudentService service) { this.service = service; }

    // Create student, optional universityId as query param
    @PostMapping
    public Student create(@RequestBody Student student, @RequestParam(required = false) Long universityId) {
        return service.create(student, universityId);
    }

    @GetMapping
    public List<Student> list() { return service.listAll(); }

    @GetMapping("/{id}")
    public Student get(@PathVariable Long id) { return service.getById(id).orElse(null); }

    // Update with optional universityId
    @PutMapping("/{id}")
    public Student update(@PathVariable Long id, @RequestBody Student student, @RequestParam(required = false) Long universityId) {
        return service.update(id, student, universityId);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) { service.delete(id); }

    @GetMapping("/search")
    public List<Student> search(@RequestParam String q) { return service.searchByName(q); }

    @GetMapping("/byUniversity")
    public List<Student> byUniversity(@RequestParam String name) { return service.byUniversityName(name); }
}
