
create database PySparkETL

GO


IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'SoundcloudUser') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
  DROP TABLE [dbo].[SoundcloudUser]
GO


CREATE TABLE [dbo].[SoundcloudUser] (
    [ID] INT IDENTITY(1,1),
	[UserName] VARCHAR(MAX),
	[Number_Follows] INT,
	[Number_Tracks] INT,
	[Link] VARCHAR(MAX)
)

GO


