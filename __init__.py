# CREATE TABLE `Customers` (
#   `userId` int NOT NULL AUTO_INCREMENT,
#   `phoneNumber` varchar(20) NOT NULL,
#   `username` varchar(70) NOT NULL,
#   `email` varchar(70) NOT NULL,
#   `contactName` varchar(70) NOT NULL,
#   `currencyCode` varchar(10) NOT NULL DEFAULT 'USD',
#   `countryCode` varchar(10) NOT NULL DEFAULT 'US',
#   `locationHash` varchar(12) NOT NULL DEFAULT '',
#   `lat` float NOT NULL DEFAULT '0',
#   `lng` float NOT NULL DEFAULT '0',
#   `address` varchar(300) NOT NULL DEFAULT '' COMMENT 'This is the address of the customer',
#   `deviceIds` text NOT NULL COMMENT 'This is a comma separated list of device ids owned by the customer',
#   `websiteUrl` varchar(200) NOT NULL DEFAULT '',
#   `organizationName` varchar(100) NOT NULL DEFAULT '' COMMENT 'This is the name of the organization which is only available for businesses',
#   `profilePicture` varchar(200) NOT NULL DEFAULT '',
#   `createdOnTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `lastUpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#   PRIMARY KEY (`userId`),
#   UNIQUE KEY `username` (`username`),
#   UNIQUE KEY `phoneNumber` (`phoneNumber`),
#   UNIQUE KEY `email` (`email`)
# ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |

# CREATE TABLE `Devices` (
#   `deviceRefNumber` int NOT NULL AUTO_INCREMENT,
#   `username` varchar(70) NOT NULL,
#   `deviceId` varchar(100) NOT NULL,
#   `deviceName` varchar(70) NOT NULL,
#   `deviceType` varchar(70) NOT NULL,
#   `deviceDescription` varchar(200) NOT NULL,
#   `defaultDeviceLocationHash` varchar(12) NOT NULL,
#   `devicePicture` varchar(200) NOT NULL DEFAULT '',
#   `subscribeToTopics` varchar(200) NOT NULL DEFAULT '' COMMENT 'This is a comma separated list of topics this device is subscribed to',
#   `createdOnTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `lastUpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#   PRIMARY KEY (`deviceRefNumber`),
#   UNIQUE KEY `deviceId` (`deviceId`),
#   KEY `username` (`username`),
#   CONSTRAINT `Devices_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Customers` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
# ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |

# CREATE TABLE `PublishedMessages` (
#   `messageId` int NOT NULL AUTO_INCREMENT COMMENT 'This is the message id and serves as the primary key',
#   `topic` varchar(200) NOT NULL COMMENT 'This is the topic',
#   `payload` text NOT NULL COMMENT 'This is the message payload',
#   `qos` int DEFAULT '0',
#   `retain` int DEFAULT '0',
#   `published_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'This is the time the message was published',
#   `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'This is the time the message was created',
#   `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'This is the time the message was updated',
#   `username` varchar(20) NOT NULL COMMENT 'This is the username of the owner of the device',
#   `client_id` varchar(200) NOT NULL COMMENT 'This is the id of the device',
#   `published_attempts` int NOT NULL DEFAULT '0' COMMENT 'This is the number of attempts to publish the message',
#   `published_outcome` int NOT NULL DEFAULT '0' COMMENT 'This is the outcome of the publish attempt',
#   `published_mid` int DEFAULT '0',
#   `published_rc` int DEFAULT '0',
#   `published_properties` text COMMENT 'These are the properties of the publish attempt',
#   PRIMARY KEY (`messageId`),
#   KEY `username` (`username`),
#   KEY `client_id` (`client_id`),
#   CONSTRAINT `PublishedMessages_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Customers` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
#   CONSTRAINT `PublishedMessages_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `Devices` (`deviceId`) ON DELETE CASCADE ON UPDATE CASCADE
# ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |

#  CREATE TABLE `Topics` (
#   `topicId` int NOT NULL AUTO_INCREMENT,
#   `topic` varchar(200) NOT NULL,
#   `description` varchar(200) NOT NULL,
#   `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#   PRIMARY KEY (`topicId`),
#   UNIQUE KEY `topic` (`topic`)
# ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci