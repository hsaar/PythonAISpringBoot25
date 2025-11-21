package org.mbc.controller.Answer;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.mbc.controller.Question.Question;

import java.time.LocalDateTime;

@Getter
@Setter
@Entity
public class Answer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(columnDefinition = "TEXT")
    private String content;

    private LocalDateTime createDate;

    @ManyToOne
    private Question question;
}
