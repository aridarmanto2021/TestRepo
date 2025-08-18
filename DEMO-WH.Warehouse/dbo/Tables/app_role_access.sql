CREATE TABLE [dbo].[app_role_access] (

	[Id] int NULL, 
	[role_id] int NULL, 
	[menu_id] int NULL, 
	[raccess_allowed] varchar(255) NULL, 
	[create_at] datetime2(3) NULL, 
	[modify_at] datetime2(3) NULL, 
	[created_by] int NULL, 
	[modified_by] int NULL
);