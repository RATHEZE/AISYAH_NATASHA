-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 01, 2024 at 04:57 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parcel_bill`
--

-- --------------------------------------------------------

--
-- Table structure for table `courier_info`
--

CREATE TABLE `courier_info` (
  `id` int(11) NOT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `parcel_type` varchar(100) DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `service_type` varchar(100) DEFAULT NULL,
  `distance` float DEFAULT NULL,
  `total_bill` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courier_info`
--

INSERT INTO `courier_info` (`id`, `customer_name`, `parcel_type`, `weight`, `service_type`, `distance`, `total_bill`) VALUES
(1, 'SITI AISYAH NATASHA', 'large box', 2, 'standard', 127, 453.5),
(2, 'NURUL SOFIAH', 'small box', 0.02, 'express', 69, 44.66),
(3, 'MUHAMMAD ADDAM', 'medium box', 0.03, 'express', 251, 261.36),
(4, 'NUR NABILA', 'small box', 0.02, 'standard', 5, 7.16),
(5, 'MUHAMMAD ALI', 'large box', 12, 'standard', 20, 224.5),
(6, 'AYEESHA WAHEEDA', 'medium box', 0.08, 'standard', 25, 30.46);

-- --------------------------------------------------------

--
-- Table structure for table `parcel_bill`
--

CREATE TABLE `parcel_bill` (
  `customer_name` varchar(100) NOT NULL,
  `parcel_type` int(200) NOT NULL,
  `weight` int(200) NOT NULL,
  `service_type` varchar(200) NOT NULL,
  `distance` int(200) NOT NULL,
  `total_bill` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `courier_info`
--
ALTER TABLE `courier_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `courier_info`
--
ALTER TABLE `courier_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
