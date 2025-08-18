CREATE TABLE [dbo].[app_user] (

	[Id] int NULL, 
	[user_name] varchar(60) NULL, 
	[user_login] varchar(30) NULL, 
	[user_password] varchar(32) NULL, 
	[user_email] varchar(160) NULL, 
	[role_id] int NULL, 
	[user_parent] int NULL, 
	[create_at] datetime2(3) NULL, 
	[modify_at] datetime2(3) NULL, 
	[created_by] int NULL, 
	[modified_by] int NULL, 
	[user_role_filter] varchar(100) NULL
);