-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 29, 2023 at 08:43 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2onlineauctiondb`
--

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `ProductId` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `QPrice` varchar(250) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `date` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `SellerName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `UserName`, `Mobile`, `ProductId`, `ProductName`, `Price`, `QPrice`, `Image`, `date`, `Status`, `SellerName`) VALUES
(1, 'san', '9486365535', '2', 'remi5g', '7000', '9000', 'ba.png', '2023-02-24', 'waiting', ''),
(2, 'san', '9486365535', '1', 'samsung55 tv', '10000', '50000', '111.jpg', '2023-02-24', 'Payment', ''),
(3, 'san', '9486365535', '1', 'samsung55 tv', '10000', '50000', '111.jpg', '2023-02-24', 'Reject', ''),
(4, 'naveen', '6383367085', '4', 'samsung55 tv', '8900', '8000', 'banner.jpg', '2023-03-02', 'Payment', 'san'),
(5, 'san', '9486365535', '4', 'samsung55 tv', '10000', '50000', '76.jpg', '2023-03-28', 'Reject', 'san');

-- --------------------------------------------------------

--
-- Table structure for table `protb`
--

CREATE TABLE `protb` (
  `id` bigint(20) NOT NULL auto_increment,
  `ProductName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `Price` varchar(20) NOT NULL,
  `Info` varchar(500) NOT NULL,
  `LastDate` date NOT NULL,
  `Image` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `SellerName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `protb`
--

INSERT INTO `protb` (`id`, `ProductName`, `ProductType`, `Price`, `Info`, `LastDate`, `Image`, `Status`, `SellerName`) VALUES
(1, 'samsung55 tv', 'TV', '10000', '1 yera', '2022-12-31', '111.jpg', 'Close', ''),
(2, 'remi5g', 'Mobile', '7000', 'sadfsa', '2023-02-28', 'ba.png', 'waiting', ''),
(3, 'samsung55 tv', 'TV', '8900', 'asdfas', '2023-03-04', 'banner.jpg', 'waiting', ''),
(4, 'samsung55 tv', 'TV', '10000', 'asf', '2023-03-29', '76.jpg', 'Close', 'san');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'Sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16 samnath plaza, melapudur  trichy\r\n', 'san', 'san'),
(2, 'balambigai', '7904902206', 'balambigai@gmail.com', 'No 16 samnath plaza, melapudur  trichy', 'balambigai', 'balambigai'),
(3, 'naveen', '09486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'naveen', 'naveen');

-- --------------------------------------------------------

--
-- Table structure for table `sellertb`
--

CREATE TABLE `sellertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `sellertb`
--

INSERT INTO `sellertb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');
