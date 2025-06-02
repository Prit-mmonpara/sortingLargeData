package com.example.sortingLargeData.repository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.example.sortingLargeData.entity.User;
import java.util.List;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    @Query("SELECT u FROM User u WHERE LOWER(u.name) LIKE LOWER(CONCAT('%', :name, '%'))")
    Page<User> findByNameContainingIgnoreCase(@Param("name") String name, Pageable pageable);
    
    // For exact match with pagination
    @Query("SELECT u FROM User u WHERE LOWER(u.name) = LOWER(:name)")
    Page<User> findByNameIgnoreCase(@Param("name") String name, Pageable pageable);

    // This interface will automatically provide CRUD operations for User entity
    // No additional methods are needed unless custom queries are required
    
}
