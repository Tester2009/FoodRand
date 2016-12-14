CREATE TABLE `foodrestaurant` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `restaurantname` text,
  `restaurantlocation` text,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO foodrestaurant (`restaurantname`, `restaurantlocation`) VALUES ('demo_name', 'demo_location');