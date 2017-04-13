-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Feb 23, 2017 at 07:20 PM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `friend_market`
--

-- --------------------------------------------------------

--
-- Table structure for table `five_min`
--

CREATE TABLE `five_min` (
  `id` int(11) NOT NULL,
  `stock_id` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `close` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `five_min`
--

INSERT INTO `five_min` (`id`, `stock_id`, `timestamp`, `close`) VALUES
(2, 1, '2017-02-23 15:29:29', 10),
(3, 2, '2017-02-23 15:30:48', 20),
(4, 1, '2017-02-23 15:31:02', 10);

-- --------------------------------------------------------

--
-- Table structure for table `stock_names`
--

CREATE TABLE `stock_names` (
  `stock_id` int(11) NOT NULL,
  `stock_name` varchar(255) NOT NULL,
  `stock_Company` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stock_names`
--

INSERT INTO `stock_names` (`stock_id`, `stock_name`, `stock_Company`) VALUES
(1, 'rushil', 'rushil pvt. LTD'),
(2, 'NCC', 'NCC PVT LTD');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `five_min`
--
ALTER TABLE `five_min`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `stock_names`
--
ALTER TABLE `stock_names`
  ADD PRIMARY KEY (`stock_id`),
  ADD UNIQUE KEY `stock_id` (`stock_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `five_min`
--
ALTER TABLE `five_min`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `stock_names`
--
ALTER TABLE `stock_names`
  MODIFY `stock_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
