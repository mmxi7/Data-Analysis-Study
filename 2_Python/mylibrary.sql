CREATE TABLE `members` (
  `id` INT PRIMARY KEY AUTO_INCREMENT COMMENT '회원 번호',
  `name` VARCHAR(50)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE `books` (
  `id` int PRIMARY KEY AUTO_INCREMENT COMMENT '도서 번호',
  `title` varchar(100) NOT NULL COMMENT '도서 제목'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE `loans` (
  `id` int PRIMARY KEY AUTO_INCREMENT COMMENT '대출 번호',
  `member_id` int NOT NULL COMMENT '대출한 회원',
  `book_id` int NOT NULL COMMENT '대출된 도서',
  `loan_date` datetime NOT NULL COMMENT '대출일시',
  `due_date` date NOT NULL COMMENT '반납 예정일',
  `return_date` date COMMENT '실제 반납일',
  `status` ENUM ('A', 'B', 'C') NOT NULL DEFAULT "A" COMMENT '대출상태(A=대출중, B=반납완료,C=연체)',
  `fine_amount` decimal(10, 2) DEFAULT 0 COMMENT '연체료',
  `auto_renewal` boolean DEFAULT false COMMENT '반납일 자동 연장 여부',
  `notes` text COMMENT '메모(특이사항)'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

ALTER TABLE `loans` ADD FOREIGN KEY (`member_id`) REFERENCES `members` (`id`);

ALTER TABLE `loans` ADD FOREIGN KEY (`book_id`) REFERENCES `books` (`id`);

ALTER TABLE `members` COMMENT = '회원';

ALTER TABLE `books` COMMENT = '도서';

ALTER TABLE `loans` COMMENT = '도서 대출';

