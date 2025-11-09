package com.example.demo.service;

import com.example.demo.entity.Student;
import com.example.demo.entity.University;
import com.example.demo.repository.StudentRepository;
import com.example.demo.repository.UniversityRepository;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class StudentService {

    private final StudentRepository studentRepo;
    private final UniversityRepository universityRepo;

    public StudentService(StudentRepository studentRepo, UniversityRepository universityRepo) {
        this.studentRepo = studentRepo;
        this.universityRepo = universityRepo;
    }

    public Student create(Student s, Long universityId) {
        if (universityId != null) {
            University u = universityRepo.findById(universityId)
                    .orElseThrow(() -> new RuntimeException("University not found id=" + universityId));
            s.setUniversity(u);
        }
        return studentRepo.save(s);
    }

    public List<Student> listAll() {
        return studentRepo.findAll();
    }

    public Optional<Student> getById(Long id) {
        return studentRepo.findById(id);
    }

    public Student update(Long id, Student updated, Long universityId) {
        Student s = studentRepo.findById(id).orElseThrow(() -> new RuntimeException("Student not found"));
        s.setFirstName(updated.getFirstName());
        s.setLastName(updated.getLastName());
        s.setEmail(updated.getEmail());
        if (universityId != null) {
            University u = universityRepo.findById(universityId).orElseThrow(() -> new RuntimeException("University not found"));
            s.setUniversity(u);
        }
        return studentRepo.save(s);
    }

    public void delete(Long id) {
        studentRepo.deleteById(id);
    }

    public List<Student> searchByName(String q) {
        if (q == null || q.isBlank()) return Collections.emptyList();
        List<Student> a = studentRepo.findByFirstNameContainingIgnoreCase(q);
        List<Student> b = studentRepo.findByLastNameContainingIgnoreCase(q);
        return StreamConcatDistinct(a, b);
    }

    public List<Student> byUniversityName(String name) {
        return studentRepo.findByUniversity_NameContainingIgnoreCase(name);
    }

    private List<Student> StreamConcatDistinct(List<Student> a, List<Student> b) {
    List<Student> result = new ArrayList<>(a);
    for (Student s : b) {
        if (!result.contains(s)) {
            result.add(s);
        }
    }
    return result;
}

}
