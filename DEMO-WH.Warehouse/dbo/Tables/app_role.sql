CREATE TABLE [dbo].[app_role] (

	[Id] int NULL, 
	[role_name] varchar(60) NULL, 
	[role_parent] int NULL, 
	[create_at] datetime2(3) NULL, 
	[modify_at] datetime2(3) NULL, 
	[created_by] int NULL, 
	[modified_by] int NULL, 
	[role_column] varchar(100) NULL
);