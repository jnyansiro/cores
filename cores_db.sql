BEGIN;
--
-- Create model Comment
--
CREATE TABLE "projects_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "comment" varchar(2500) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL);
--
-- Create model Dislike
--
CREATE TABLE "projects_dislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "dislike" bool NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL);
--
-- Create model Goal
--
CREATE TABLE "projects_goal" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "goal_name" varchar(50) NOT NULL, "description" varchar(2300) NULL, "category" varchar(50) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL);
--
-- Create model Incentive
--
CREATE TABLE "projects_incentive" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "incentive_type" varchar(50) NOT NULL, "description" varchar(500) NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL);
--
-- Create model Like
--
CREATE TABLE "projects_like" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "like" bool NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL);
--
-- Create model Member
--
CREATE TABLE "projects_member" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(50) NOT NULL, "middle_name" varchar(50) NOT NULL, "surname" varchar(50) NOT NULL, "phone" varchar(12) NOT NULL, "country" varchar(50) NOT NULL, "professional" varchar(50) NOT NULL, "job_title" varchar(50) NOT NULL, "institution_name" varchar(50) NOT NULL, "profile_photo" varchar(50) NOT NULL, "created_on" date NOT NULL, "update_on" date NOT NULL);
--
-- Create model Process
--
CREATE TABLE "projects_process" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "file" varchar(500) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Project
--
CREATE TABLE "projects_project" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "project_title" varchar(50) NOT NULL, "description" varchar(2500) NOT NULL, "due_date" date NOT NULL, "sector" varchar(50) NOT NULL, "is_public" bool NOT NULL, "is_private" bool NOT NULL, "is_discoverable" bool NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Requirement
--
CREATE TABLE "projects_requirement" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "description" varchar(2500) NOT NULL, "file" varchar(500) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "goal_id" integer NOT NULL REFERENCES "projects_goal" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RequirementArtifact
--
CREATE TABLE "projects_requirementartifact" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "artifact_type" varchar(50) NOT NULL, "artifact_content" varchar(500) NOT NULL, "artifact_link" varchar(200) NULL, "uploaded_file" varchar(50) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "requirement_id" integer NOT NULL REFERENCES "projects_requirement" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Scenario
--
CREATE TABLE "projects_scenario" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "description" varchar(1500) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "requirement_id" integer NOT NULL REFERENCES "projects_requirement" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model StarRate
--
CREATE TABLE "projects_starrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "number_of_stars" integer NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "rated_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model UseCase
--
CREATE TABLE "projects_usecase" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "usecase_name" varchar(50) NOT NULL, "description" varchar(500) NOT NULL, "file" varchar(500) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "process_id" integer NOT NULL REFERENCES "projects_process" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model User
--
CREATE TABLE "projects_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "username" varchar(50) NOT NULL UNIQUE, "email" varchar(50) NOT NULL, "password" varchar(50) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL);
--
-- Create model Viewpoint
--
CREATE TABLE "projects_viewpoint" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "viewpoint_name" varchar(50) NOT NULL, "description" varchar(2300) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ViewPointRate
--
CREATE TABLE "projects_viewpointrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "star_rate_id" integer NOT NULL REFERENCES "projects_starrate" ("id") DEFERRABLE INITIALLY DEFERRED, "view_point_id" integer NOT NULL REFERENCES "projects_viewpoint" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ViewpointLike
--
CREATE TABLE "projects_viewpointlike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED, "view_point_id" integer NOT NULL REFERENCES "projects_viewpoint" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ViewpointDislike
--
CREATE TABLE "projects_viewpointdislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED, "view_point_id" integer NOT NULL REFERENCES "projects_viewpoint" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ViewPointComment
--
CREATE TABLE "projects_viewpointcomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "viewpoint_id" integer NOT NULL REFERENCES "projects_viewpoint" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model UseCaseRate
--
CREATE TABLE "projects_usecaserate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "star_rate_id" integer NOT NULL REFERENCES "projects_starrate" ("id") DEFERRABLE INITIALLY DEFERRED, "usecase_id" integer NOT NULL REFERENCES "projects_usecase" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model UseCaseLike
--
CREATE TABLE "projects_usecaselike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED, "use_case_id" integer NOT NULL REFERENCES "projects_usecase" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model UseCaseDislike
--
CREATE TABLE "projects_usecasedislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED, "use_case_id" integer NOT NULL REFERENCES "projects_usecase" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model UseCaseComment
--
CREATE TABLE "projects_usecasecomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "usecase_id" integer NOT NULL REFERENCES "projects_usecase" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ScenarioRate
--
CREATE TABLE "projects_scenariorate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "scenario_id" integer NOT NULL REFERENCES "projects_scenario" ("id") DEFERRABLE INITIALLY DEFERRED, "star_rate_id" integer NOT NULL REFERENCES "projects_starrate" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ScenarioLike
--
CREATE TABLE "projects_scenariolike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED, "scenario_id" integer NOT NULL REFERENCES "projects_scenario" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ScenarioDislike
--
CREATE TABLE "projects_scenariodislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED, "scenario_id" integer NOT NULL REFERENCES "projects_scenario" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ScenarioComment
--
CREATE TABLE "projects_scenariocomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "scenario_id" integer NOT NULL REFERENCES "projects_scenario" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RequiremetDislike
--
CREATE TABLE "projects_requiremetdislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED, "requirement_id" integer NOT NULL REFERENCES "projects_requirement" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RequirementRate
--
CREATE TABLE "projects_requirementrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "requirement_id" integer NOT NULL REFERENCES "projects_requirement" ("id") DEFERRABLE INITIALLY DEFERRED, "star_rate_id" integer NOT NULL REFERENCES "projects_starrate" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RequirementLike
--
CREATE TABLE "projects_requirementlike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED, "requirement_id" integer NOT NULL REFERENCES "projects_requirement" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RequirementComment
--
CREATE TABLE "projects_requirementcomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "requirement_id" integer NOT NULL REFERENCES "projects_requirement" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RequirementArtifactRate
--
CREATE TABLE "projects_requirementartifactrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "requiremet_artifact_id" integer NOT NULL REFERENCES "projects_requirementartifact" ("id") DEFERRABLE INITIALLY DEFERRED, "star_rate_id" integer NOT NULL REFERENCES "projects_starrate" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RequirementArtifactLike
--
CREATE TABLE "projects_requirementartifactlike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED, "requirement_artifact_id" integer NOT NULL REFERENCES "projects_requirementartifact" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model RequirementArtifactDislike
--
CREATE TABLE "projects_requirementartifactdislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED, "requirement_artifact_id" integer NOT NULL REFERENCES "projects_requirementartifact" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Repository
--
CREATE TABLE "projects_repository" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "resource_name" varchar(500) NOT NULL, "resource_type" varchar(50) NOT NULL, "description" varchar(500) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "added_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProjectRate
--
CREATE TABLE "projects_projectrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED, "star_rate_id" integer NOT NULL REFERENCES "projects_starrate" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProjectMembership
--
CREATE TABLE "projects_projectmembership" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "member_role" varchar(50) NOT NULL, "status" varchar(50) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "member_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProjectLike
--
CREATE TABLE "projects_projectlike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProjectIncentive
--
CREATE TABLE "projects_projectincentive" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "unit" varchar(50) NULL, "amount" varchar(50) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "incentive_id" integer NOT NULL REFERENCES "projects_incentive" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProjectDislike
--
CREATE TABLE "projects_projectdislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProjectComment
--
CREATE TABLE "projects_projectcomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProcessRate
--
CREATE TABLE "projects_processrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "process_id" integer NOT NULL REFERENCES "projects_process" ("id") DEFERRABLE INITIALLY DEFERRED, "star_rate_id" integer NOT NULL REFERENCES "projects_starrate" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProcessLike
--
CREATE TABLE "projects_processlike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED, "process_id" integer NOT NULL REFERENCES "projects_process" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProcessDislike
--
CREATE TABLE "projects_processdislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED, "process_id" integer NOT NULL REFERENCES "projects_process" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProcessComment
--
CREATE TABLE "projects_processcomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "process_id" integer NOT NULL REFERENCES "projects_process" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field scenario to process
--
CREATE TABLE "new__projects_process" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "file" varchar(500) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "scenario_id" integer NOT NULL REFERENCES "projects_scenario" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__projects_process" ("id", "file", "created_on", "updated_on", "created_by_id", "scenario_id") SELECT "id", "file", "created_on", "updated_on", "created_by_id", NULL FROM "projects_process";
DROP TABLE "projects_process";
ALTER TABLE "new__projects_process" RENAME TO "projects_process";
CREATE INDEX "projects_project_created_by_id_c49d7b6d" ON "projects_project" ("created_by_id");
CREATE INDEX "projects_requirement_created_by_id_66b6d9cb" ON "projects_requirement" ("created_by_id");
CREATE INDEX "projects_requirement_goal_id_164974c9" ON "projects_requirement" ("goal_id");
CREATE INDEX "projects_requirementartifact_created_by_id_d4ca9855" ON "projects_requirementartifact" ("created_by_id");
CREATE INDEX "projects_requirementartifact_requirement_id_eee6e10e" ON "projects_requirementartifact" ("requirement_id");
CREATE INDEX "projects_scenario_created_by_id_b3922e64" ON "projects_scenario" ("created_by_id");
CREATE INDEX "projects_scenario_requirement_id_1913cdeb" ON "projects_scenario" ("requirement_id");
CREATE INDEX "projects_starrate_rated_by_id_71f8f295" ON "projects_starrate" ("rated_by_id");
CREATE INDEX "projects_usecase_created_by_id_ef34290d" ON "projects_usecase" ("created_by_id");
CREATE INDEX "projects_usecase_process_id_4b44d42a" ON "projects_usecase" ("process_id");
CREATE INDEX "projects_viewpoint_created_by_id_8eb08a28" ON "projects_viewpoint" ("created_by_id");
CREATE INDEX "projects_viewpoint_project_id_3fceed54" ON "projects_viewpoint" ("project_id");
CREATE INDEX "projects_viewpointrate_star_rate_id_26c76cab" ON "projects_viewpointrate" ("star_rate_id");
CREATE INDEX "projects_viewpointrate_view_point_id_20805d29" ON "projects_viewpointrate" ("view_point_id");
CREATE INDEX "projects_viewpointlike_like_id_04355a7f" ON "projects_viewpointlike" ("like_id");
CREATE INDEX "projects_viewpointlike_view_point_id_7151d885" ON "projects_viewpointlike" ("view_point_id");
CREATE INDEX "projects_viewpointdislike_dislike_id_8eaf1363" ON "projects_viewpointdislike" ("dislike_id");
CREATE INDEX "projects_viewpointdislike_view_point_id_f2030939" ON "projects_viewpointdislike" ("view_point_id");
CREATE INDEX "projects_viewpointcomment_comment_id_16deee4a" ON "projects_viewpointcomment" ("comment_id");
CREATE INDEX "projects_viewpointcomment_viewpoint_id_c3fa0dc0" ON "projects_viewpointcomment" ("viewpoint_id");
CREATE INDEX "projects_usecaserate_star_rate_id_158f3c75" ON "projects_usecaserate" ("star_rate_id");
CREATE INDEX "projects_usecaserate_usecase_id_1592322a" ON "projects_usecaserate" ("usecase_id");
CREATE INDEX "projects_usecaselike_like_id_9296daad" ON "projects_usecaselike" ("like_id");
CREATE INDEX "projects_usecaselike_use_case_id_377f5f41" ON "projects_usecaselike" ("use_case_id");
CREATE INDEX "projects_usecasedislike_dislike_id_20d08a8d" ON "projects_usecasedislike" ("dislike_id");
CREATE INDEX "projects_usecasedislike_use_case_id_c7979d6a" ON "projects_usecasedislike" ("use_case_id");
CREATE INDEX "projects_usecasecomment_comment_id_ef85ef8a" ON "projects_usecasecomment" ("comment_id");
CREATE INDEX "projects_usecasecomment_usecase_id_b805a32f" ON "projects_usecasecomment" ("usecase_id");
CREATE INDEX "projects_scenariorate_scenario_id_aa0a5077" ON "projects_scenariorate" ("scenario_id");
CREATE INDEX "projects_scenariorate_star_rate_id_6cec826e" ON "projects_scenariorate" ("star_rate_id");
CREATE INDEX "projects_scenariolike_like_id_acd471ad" ON "projects_scenariolike" ("like_id");
CREATE INDEX "projects_scenariolike_scenario_id_d5293a32" ON "projects_scenariolike" ("scenario_id");
CREATE INDEX "projects_scenariodislike_dislike_id_d83ffba6" ON "projects_scenariodislike" ("dislike_id");
CREATE INDEX "projects_scenariodislike_scenario_id_8ab0e652" ON "projects_scenariodislike" ("scenario_id");
CREATE INDEX "projects_scenariocomment_comment_id_25864f0b" ON "projects_scenariocomment" ("comment_id");
CREATE INDEX "projects_scenariocomment_scenario_id_9373d970" ON "projects_scenariocomment" ("scenario_id");
CREATE INDEX "projects_requiremetdislike_dislike_id_1ef98473" ON "projects_requiremetdislike" ("dislike_id");
CREATE INDEX "projects_requiremetdislike_requirement_id_1c21d605" ON "projects_requiremetdislike" ("requirement_id");
CREATE INDEX "projects_requirementrate_requirement_id_7ae3a33a" ON "projects_requirementrate" ("requirement_id");
CREATE INDEX "projects_requirementrate_star_rate_id_6d22588e" ON "projects_requirementrate" ("star_rate_id");
CREATE INDEX "projects_requirementlike_like_id_5f6d94e6" ON "projects_requirementlike" ("like_id");
CREATE INDEX "projects_requirementlike_requirement_id_e45c6fd3" ON "projects_requirementlike" ("requirement_id");
CREATE INDEX "projects_requirementcomment_comment_id_305018d8" ON "projects_requirementcomment" ("comment_id");
CREATE INDEX "projects_requirementcomment_requirement_id_32a0b1b9" ON "projects_requirementcomment" ("requirement_id");
CREATE INDEX "projects_requirementartifactrate_requiremet_artifact_id_655347b0" ON "projects_requirementartifactrate" ("requiremet_artifact_id");
CREATE INDEX "projects_requirementartifactrate_star_rate_id_5fdae275" ON "projects_requirementartifactrate" ("star_rate_id");
CREATE INDEX "projects_requirementartifactlike_like_id_144dfb06" ON "projects_requirementartifactlike" ("like_id");
CREATE INDEX "projects_requirementartifactlike_requirement_artifact_id_f222b26b" ON "projects_requirementartifactlike" ("requirement_artifact_id");
CREATE INDEX "projects_requirementartifactdislike_dislike_id_b3aa0b33" ON "projects_requirementartifactdislike" ("dislike_id");
CREATE INDEX "projects_requirementartifactdislike_requirement_artifact_id_efbfcb10" ON "projects_requirementartifactdislike" ("requirement_artifact_id");
CREATE INDEX "projects_repository_added_by_id_6ffe1ff1" ON "projects_repository" ("added_by_id");
CREATE INDEX "projects_repository_project_id_a2aab11f" ON "projects_repository" ("project_id");
CREATE INDEX "projects_projectrate_project_id_87a62e98" ON "projects_projectrate" ("project_id");
CREATE INDEX "projects_projectrate_star_rate_id_b0ac7c7c" ON "projects_projectrate" ("star_rate_id");
CREATE INDEX "projects_projectmembership_member_id_50a38c52" ON "projects_projectmembership" ("member_id");
CREATE INDEX "projects_projectmembership_project_id_ec39ff46" ON "projects_projectmembership" ("project_id");
CREATE INDEX "projects_projectlike_like_id_1c64da44" ON "projects_projectlike" ("like_id");
CREATE INDEX "projects_projectlike_project_id_ba72a36b" ON "projects_projectlike" ("project_id");
CREATE INDEX "projects_projectincentive_incentive_id_e983f2cd" ON "projects_projectincentive" ("incentive_id");
CREATE INDEX "projects_projectincentive_project_id_fa1c109d" ON "projects_projectincentive" ("project_id");
CREATE INDEX "projects_projectdislike_dislike_id_7d0fa69f" ON "projects_projectdislike" ("dislike_id");
CREATE INDEX "projects_projectdislike_project_id_ad93167b" ON "projects_projectdislike" ("project_id");
CREATE INDEX "projects_projectcomment_comment_id_3e026006" ON "projects_projectcomment" ("comment_id");
CREATE INDEX "projects_projectcomment_project_id_c9cb523e" ON "projects_projectcomment" ("project_id");
CREATE INDEX "projects_processrate_process_id_7453275a" ON "projects_processrate" ("process_id");
CREATE INDEX "projects_processrate_star_rate_id_a1af9ba9" ON "projects_processrate" ("star_rate_id");
CREATE INDEX "projects_processlike_like_id_b02d424d" ON "projects_processlike" ("like_id");
CREATE INDEX "projects_processlike_process_id_b991b32a" ON "projects_processlike" ("process_id");
CREATE INDEX "projects_processdislike_dislike_id_57721745" ON "projects_processdislike" ("dislike_id");
CREATE INDEX "projects_processdislike_process_id_a81eef02" ON "projects_processdislike" ("process_id");
CREATE INDEX "projects_processcomment_comment_id_e47dd768" ON "projects_processcomment" ("comment_id");
CREATE INDEX "projects_processcomment_process_id_6ee3631f" ON "projects_processcomment" ("process_id");
CREATE INDEX "projects_process_created_by_id_c4cb3ab2" ON "projects_process" ("created_by_id");
CREATE INDEX "projects_process_scenario_id_b0a7cf0c" ON "projects_process" ("scenario_id");
--
-- Add field user to member
--
CREATE TABLE "new__projects_member" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(50) NOT NULL, "middle_name" varchar(50) NOT NULL, "surname" varchar(50) NOT NULL, "phone" varchar(12) NOT NULL, "country" varchar(50) NOT NULL, "professional" varchar(50) NOT NULL, "job_title" varchar(50) NOT NULL, "institution_name" varchar(50) NOT NULL, "profile_photo" varchar(50) NOT NULL, "created_on" date NOT NULL, "update_on" date NOT NULL, "user_id" integer NOT NULL REFERENCES "projects_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__projects_member" ("id", "first_name", "middle_name", "surname", "phone", "country", "professional", "job_title", "institution_name", "profile_photo", "created_on", "update_on", "user_id") SELECT "id", "first_name", "middle_name", "surname", "phone", "country", "professional", "job_title", "institution_name", "profile_photo", "created_on", "update_on", NULL FROM "projects_member";
DROP TABLE "projects_member";
ALTER TABLE "new__projects_member" RENAME TO "projects_member";
CREATE INDEX "projects_member_user_id_d342231d" ON "projects_member" ("user_id");
--
-- Create model LoginLog
--
CREATE TABLE "projects_loginlog" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "login_time" datetime NOT NULL, "logout_time" datetime NOT NULL, "created_on" date NOT NULL, "user_id" integer NOT NULL REFERENCES "projects_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field liked_by to like
--
CREATE TABLE "new__projects_like" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "like" bool NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "liked_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__projects_like" ("id", "like", "created_on", "updated_on", "liked_by_id") SELECT "id", "like", "created_on", "updated_on", NULL FROM "projects_like";
DROP TABLE "projects_like";
ALTER TABLE "new__projects_like" RENAME TO "projects_like";
CREATE INDEX "projects_loginlog_user_id_faebbe44" ON "projects_loginlog" ("user_id");
CREATE INDEX "projects_like_liked_by_id_0c775556" ON "projects_like" ("liked_by_id");
--
-- Add field created_by to incentive
--
CREATE TABLE "new__projects_incentive" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "incentive_type" varchar(50) NOT NULL, "description" varchar(500) NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__projects_incentive" ("id", "incentive_type", "description", "created_on", "updated_on", "created_by_id") SELECT "id", "incentive_type", "description", "created_on", "updated_on", NULL FROM "projects_incentive";
DROP TABLE "projects_incentive";
ALTER TABLE "new__projects_incentive" RENAME TO "projects_incentive";
CREATE INDEX "projects_incentive_created_by_id_b43bdfae" ON "projects_incentive" ("created_by_id");
--
-- Create model GoalRate
--
CREATE TABLE "projects_goalrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "goal_id" integer NOT NULL REFERENCES "projects_goal" ("id") DEFERRABLE INITIALLY DEFERRED, "star_rate_id" integer NOT NULL REFERENCES "projects_starrate" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model GoalLike
--
CREATE TABLE "projects_goallike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "goal_id" integer NOT NULL REFERENCES "projects_goal" ("id") DEFERRABLE INITIALLY DEFERRED, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model GoalDislike
--
CREATE TABLE "projects_goaldislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED, "goal_id" integer NOT NULL REFERENCES "projects_goal" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model GoalComment
--
CREATE TABLE "projects_goalcomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "goal_id" integer NOT NULL REFERENCES "projects_goal" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field created_by to goal
--
CREATE TABLE "new__projects_goal" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "goal_name" varchar(50) NOT NULL, "description" varchar(2300) NULL, "category" varchar(50) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__projects_goal" ("id", "goal_name", "description", "category", "created_on", "updated_on", "created_by_id") SELECT "id", "goal_name", "description", "category", "created_on", "updated_on", NULL FROM "projects_goal";
DROP TABLE "projects_goal";
ALTER TABLE "new__projects_goal" RENAME TO "projects_goal";
CREATE INDEX "projects_goalrate_goal_id_079d4e47" ON "projects_goalrate" ("goal_id");
CREATE INDEX "projects_goalrate_star_rate_id_b1b9bcb0" ON "projects_goalrate" ("star_rate_id");
CREATE INDEX "projects_goallike_goal_id_1d2b71a8" ON "projects_goallike" ("goal_id");
CREATE INDEX "projects_goallike_like_id_077cf9a4" ON "projects_goallike" ("like_id");
CREATE INDEX "projects_goaldislike_dislike_id_c3afe981" ON "projects_goaldislike" ("dislike_id");
CREATE INDEX "projects_goaldislike_goal_id_07934709" ON "projects_goaldislike" ("goal_id");
CREATE INDEX "projects_goalcomment_comment_id_a06adbb6" ON "projects_goalcomment" ("comment_id");
CREATE INDEX "projects_goalcomment_goal_id_950dcd7b" ON "projects_goalcomment" ("goal_id");
CREATE INDEX "projects_goal_created_by_id_66ba60ee" ON "projects_goal" ("created_by_id");
--
-- Add field viewpoint to goal
--
CREATE TABLE "new__projects_goal" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "goal_name" varchar(50) NOT NULL, "description" varchar(2300) NULL, "category" varchar(50) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "created_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED, "viewpoint_id" integer NOT NULL REFERENCES "projects_viewpoint" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__projects_goal" ("id", "goal_name", "description", "category", "created_on", "updated_on", "created_by_id", "viewpoint_id") SELECT "id", "goal_name", "description", "category", "created_on", "updated_on", "created_by_id", NULL FROM "projects_goal";
DROP TABLE "projects_goal";
ALTER TABLE "new__projects_goal" RENAME TO "projects_goal";
CREATE INDEX "projects_goal_created_by_id_66ba60ee" ON "projects_goal" ("created_by_id");
CREATE INDEX "projects_goal_viewpoint_id_f1593c89" ON "projects_goal" ("viewpoint_id");
--
-- Add field disliked_by to dislike
--
CREATE TABLE "new__projects_dislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "dislike" bool NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "disliked_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__projects_dislike" ("id", "dislike", "created_on", "updated_on", "disliked_by_id") SELECT "id", "dislike", "created_on", "updated_on", NULL FROM "projects_dislike";
DROP TABLE "projects_dislike";
ALTER TABLE "new__projects_dislike" RENAME TO "projects_dislike";
CREATE INDEX "projects_dislike_disliked_by_id_6613303d" ON "projects_dislike" ("disliked_by_id");
--
-- Create model CommentLike
--
CREATE TABLE "projects_commentlike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "like_id" integer NOT NULL REFERENCES "projects_like" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model CommentDislike
--
CREATE TABLE "projects_commentdislike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "dislike_id" integer NOT NULL REFERENCES "projects_dislike" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field commented_by to comment
--
CREATE TABLE "new__projects_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "comment" varchar(2500) NOT NULL, "created_on" date NOT NULL, "updated_on" date NOT NULL, "commented_by_id" integer NOT NULL REFERENCES "projects_member" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__projects_comment" ("id", "comment", "created_on", "updated_on", "commented_by_id") SELECT "id", "comment", "created_on", "updated_on", NULL FROM "projects_comment";
DROP TABLE "projects_comment";
ALTER TABLE "new__projects_comment" RENAME TO "projects_comment";
CREATE INDEX "projects_commentlike_comment_id_38a6efe0" ON "projects_commentlike" ("comment_id");
CREATE INDEX "projects_commentlike_like_id_7458c452" ON "projects_commentlike" ("like_id");
CREATE INDEX "projects_commentdislike_comment_id_490252bc" ON "projects_commentdislike" ("comment_id");
CREATE INDEX "projects_commentdislike_dislike_id_e60e27df" ON "projects_commentdislike" ("dislike_id");
CREATE INDEX "projects_comment_commented_by_id_8b0c1ff5" ON "projects_comment" ("commented_by_id");
--
-- Create model ArtifactComment
--
CREATE TABLE "projects_artifactcomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" date NOT NULL, "updated_on" date NOT NULL, "comment_id" integer NOT NULL REFERENCES "projects_comment" ("id") DEFERRABLE INITIALLY DEFERRED, "requirement_artifact_id" integer NOT NULL REFERENCES "projects_requirementartifact" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ActivityLog
--
CREATE TABLE "projects_activitylog" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "activity" varchar(500) NOT NULL, "activity_time" datetime NOT NULL, "created_on" date NOT NULL, "user_id" integer NOT NULL REFERENCES "projects_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "projects_artifactcomment_comment_id_4fff3de3" ON "projects_artifactcomment" ("comment_id");
CREATE INDEX "projects_artifactcomment_requirement_artifact_id_4f332762" ON "projects_artifactcomment" ("requirement_artifact_id");
CREATE INDEX "projects_activitylog_user_id_50ff0b3e" ON "projects_activitylog" ("user_id");
COMMIT;
