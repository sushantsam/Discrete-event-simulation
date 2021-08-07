% IE 522
rho=0.5:0.01:0.99;
%se=repmat(1:10,1,length(rho),1)';
se=1;
m= (4*rho./(1-rho).^4)./se.^2;

plot(rho,m,'LineWidth',2);

xlabel('\rho');
ylabel('m (simulation length)');
xline(1,'--');
xlim([0.49,1.01]);
max_val=max(m);
ylim([-max_val/10,max_val]);
title('m vs \rho for a particular standard error value');
%legend('Standard error');
saveas(gcf,'hw1.jpg');


%%
%rho=0.5:0.001:0.999;
re = 1;
m_2=4./(rho.*(1-rho).^2*re^2);

figure;
plot(rho,m_2,'LineWidth',2);
% hold on;
% plot(rho,m_2,'LineWidth',2);

xlabel('\rho');
ylabel('m (simulation length)');
xline(1,'--');
xlim([0.49,1.01]);
max_val=max(m_2);
ylim([-max_val/10,max_val]);
title('m vs \rho for a particular relative error value');
%legend('Relative error');
saveas(gcf,'hw1_2.jpg');
%% 
%poissinv(0.005,10);
